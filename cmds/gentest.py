# -*- coding: utf-8 -*-
from __future__ import with_statement
import os
import re
import urllib
from distutils.cmd import Command


TESTCASE_TEMPLATE = u''\
'''# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class {name}TestCase(HangulizeTestCase):
    """ {url} """

    def setUp(self):
        from hangulize.langs.{locale} import {name}
        self.lang = {name}()
    {body}'''
TEST_METHOD_TEMPLATE = u''\
'''
    def test_{testname}(self):
        """{title}{body}"""{assertions}
'''
CODE_SEP = u'\n        '
ASSERTION_TEMPLATE = u"assert u'{want}' == self.hangulize(u'{word}')"


class gen_test(Command):

    user_options = [('url=', 'a', 'the rules url'),
                    ('name=', 'n', 'the language name'),
                    ('locale=', 'l', 'the locale code')]

    def initialize_options(self):
        self.url = None
        self.name = None
        self.locale = None

    def finalize_options(self):
        pass

    def run(self):
        if not self.url:
            self.url = raw_input('Rules URL(http://korean.go.kr/...): ')
        if not self.name:
            self.name = raw_input('Language Name(ex. Italian): ')
        if not self.locale:
            self.locale = raw_input('Locale Code(ex. it): ')
        path = os.path.join('tests', '%s.dist.py' % self.locale)
        with open(path, 'w') as out:
            print 'generating test suite...',
            print>>out, generate_testsuite(self.url,
                                           self.name,
                                           self.locale).encode('utf-8')
            print 'done'
            print 'test suite was built at %s' % path


def ordinalth(n):
    last = n - n / 10 * 10
    if last == 1:
        return '%dst' % n
    elif last == 2:
        return '%dnd' % n
    elif last == 3:
        return '%drd' % n
    return '%dth' % n


def generate_testsuite(url, name, locale):
    from BeautifulSoup import BeautifulSoup
    html = ''.join(urllib.urlopen(url).readlines())
    soup = BeautifulSoup(html)
    def need(tag):
        return tag.name == 'h3' and tag.get('class') in ('big', 'clear') or \
               tag.name == 'h4' and len(tag.attrs) == 0 or \
               tag.name == 'p' and tag.get('class') == 'h3Text' or \
               tag.name == 'li' and tag.parent.parent.get('class') in \
               ('jamobox', 'rulebox01')
    def text(tag):
        return ''.join(e for e in tag.recursiveChildGenerator() \
                         if isinstance(e, unicode))
    rules = []
    examples = {}
    body = []
    for tag in soup.findAll(need):
        if tag.get('class') == 'big':
            header = text(tag)
        elif tag.get('class') == 'clear':
            rules.append([text(tag)])
        elif tag.name in ('h4', 'p'):
            rules[-1].append(text(tag))
        elif tag.name == 'li':
            i = len(rules) - 1
            if not examples.get(i):
                examples[i] = []
            examples[i].append(text(tag))
    for i, rule in enumerate(rules):
        assertions = []
        for x in examples[i]:
            match = re.match('(?:\(.+\) )?([^ ]+) (.+)', x)
            if not match:
                assertions.append('# %s' % x)
                continue
            assertion = ASSERTION_TEMPLATE.format(want=match.group(2),
                                                  word=match.group(1))
            assertions.append(assertion)
        testname = ordinalth(int(re.search('\d+', rule[0]).group(0)))
        title = re.sub(u'(제\d+항)(?=.)', r'\1: ', rule[0])
        if len(rule) > 1:
            rulebody = CODE_SEP + CODE_SEP.join(s for s in rule[1:]) + CODE_SEP
        else:
            rulebody = ''
        if assertions:
            assertions = CODE_SEP + CODE_SEP.join(assertions)
        else:
            assertions = ''
        method = TEST_METHOD_TEMPLATE.format(testname=testname,
                                             title=title,
                                             body=rulebody,
                                             assertions=assertions)
        body.append(method)
    body = ''.join(body).strip()

    return TESTCASE_TEMPLATE.format(name=name, locale=locale,
                                    url=url, body=body)
