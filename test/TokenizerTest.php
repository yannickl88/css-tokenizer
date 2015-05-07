<?php
namespace Yannickl88\Component\CSS;

/**
 * @covers Yannickl88\Component\CSS\Tokenizer
 */
class TokenizerTest extends \PHPUnit_Framework_TestCase
{
    public function testGetWhitespaces()
    {
        $this->assertEquals([' ', "\n", "\t", "\r", "\f"], Tokenizer::getWhitespaces());
    }

    public function testParse()
    {
        $tokens = (new Tokenizer())->tokenize('span { padding: 2px; margin: 2px; }');

        $this->assertEquals([
            new Token(Token::T_WORD, 'span', 1, 1, 1, 4),
            new Token(Token::T_WHITESPACE, ' ', 1, 5),
            new Token(Token::T_OPENCURLY, '{', 1, 6),
            new Token(Token::T_WHITESPACE, ' ', 1, 7),
            new Token(Token::T_WORD, 'padding', 1, 8, 1, 14),
            new Token(Token::T_COLON, ':', 1, 15),
            new Token(Token::T_WHITESPACE, ' ', 1, 16),
            new Token(Token::T_WORD, '2px', 1, 17, 1, 19),
            new Token(Token::T_SEMICOLON, ';', 1, 20),
            new Token(Token::T_WHITESPACE, ' ', 1, 21),
            new Token(Token::T_WORD, 'margin', 1, 22, 1, 27),
            new Token(Token::T_COLON, ':', 1, 28),
            new Token(Token::T_WHITESPACE, ' ', 1, 29),
            new Token(Token::T_WORD, '2px', 1, 30, 1, 32),
            new Token(Token::T_SEMICOLON, ';', 1, 33),
            new Token(Token::T_WHITESPACE, ' ', 1, 34),
            new Token(Token::T_CLOSECURLY, '}', 1, 35),
        ], $tokens);
    }

    public function testParseURL()
    {
        $tokens = (new Tokenizer())->tokenize('span { background: url(foobar.jpg); }');

        $this->assertEquals([
            new Token(Token::T_WORD, 'span', 1, 1, 1, 4),
            new Token(Token::T_WHITESPACE, ' ', 1, 5),
            new Token(Token::T_OPENCURLY, '{', 1, 6),
            new Token(Token::T_WHITESPACE, ' ', 1, 7),
            new Token(Token::T_WORD, 'background', 1, 8, 1, 17),
            new Token(Token::T_COLON, ':', 1, 18),
            new Token(Token::T_WHITESPACE, ' ', 1, 19),
            new Token(Token::T_WORD, 'url', 1, 20, 1, 22),
            new Token(Token::T_OPENBRACKET, '(', 1, 23),
            new Token(Token::T_WORD, 'foobar.jpg', 1, 24, 1, 33),
            new Token(Token::T_CLOSEBRACKET, ')', 1, 34),
            new Token(Token::T_SEMICOLON, ';', 1, 35),
            new Token(Token::T_WHITESPACE, ' ', 1, 36),
            new Token(Token::T_CLOSECURLY, '}', 1, 37),
        ], $tokens);
    }

    public function testParseMediaQuery()
    {
        $tokens = (new Tokenizer())->tokenize(
            "@media screen and (max-width: 300px) {\n    body {\n        background-color: lightblue;\n    }\n}"
        );

        $this->assertEquals([
            new Token(Token::T_ATWORD, '@media', 1, 1, 1, 6),
            new Token(Token::T_WHITESPACE, ' ', 1, 7),
            new Token(Token::T_WORD, 'screen', 1, 8, 1, 13),
            new Token(Token::T_WHITESPACE, ' ', 1, 14),
            new Token(Token::T_WORD, 'and', 1, 15, 1, 17),
            new Token(Token::T_WHITESPACE, ' ', 1, 18),
            new Token(Token::T_OPENBRACKET, '(', 1, 19),
            new Token(Token::T_WORD, 'max-width', 1, 20, 1, 28),
            new Token(Token::T_COLON, ':', 1, 29),
            new Token(Token::T_WHITESPACE, ' ', 1, 30),
            new Token(Token::T_WORD, '300px', 1, 31, 1, 35),
            new Token(Token::T_CLOSEBRACKET, ')', 1, 36),
            new Token(Token::T_WHITESPACE, ' ', 1, 37),
            new Token(Token::T_OPENCURLY, '{', 1, 38),
            new Token(Token::T_WHITESPACE, "\n    ", 2, 0),
            new Token(Token::T_WORD, 'body', 2, 5, 2, 8),
            new Token(Token::T_WHITESPACE, ' ', 2, 9),
            new Token(Token::T_OPENCURLY, '{', 2, 10),
            new Token(Token::T_WHITESPACE, "\n        ", 3, 0),
            new Token(Token::T_WORD, 'background-color', 3, 9, 3, 24),
            new Token(Token::T_COLON, ':', 3, 25),
            new Token(Token::T_WHITESPACE, ' ', 3, 26),
            new Token(Token::T_WORD, 'lightblue', 3, 27, 3, 35),
            new Token(Token::T_SEMICOLON, ';', 3, 36),
            new Token(Token::T_WHITESPACE, "\n    ", 4, 0),
            new Token(Token::T_CLOSECURLY, '}', 4, 5),
            new Token(Token::T_WHITESPACE, "\n", 5, 0),
            new Token(Token::T_CLOSECURLY, '}', 5, 1),
        ], $tokens);
    }

    public function testParseComment()
    {
        $tokens = (new Tokenizer())->tokenize("/* foobar */");

        $this->assertEquals([
            new Token(Token::T_COMMENT, '/* foobar */', 1, 1, 1, 12),
        ], $tokens);
    }

    public function testParseCommentMultiline()
    {
        $tokens = (new Tokenizer())->tokenize("/* foo\n *\n * bar */");

        $this->assertEquals([
            new Token(Token::T_COMMENT, "/* foo\n *\n * bar */", 1, 1, 3, 9),
        ], $tokens);
    }

    public function testParseString()
    {
        $tokens = (new Tokenizer())->tokenize("span { content: \"f\\\"oo\"; }");

        $this->assertEquals([
            new Token(Token::T_WORD, 'span', 1, 1, 1, 4),
            new Token(Token::T_WHITESPACE, ' ', 1, 5),
            new Token(Token::T_OPENCURLY, '{', 1, 6),
            new Token(Token::T_WHITESPACE, ' ', 1, 7),
            new Token(Token::T_WORD, 'content', 1, 8, 1, 14),
            new Token(Token::T_COLON, ':', 1, 15),
            new Token(Token::T_WHITESPACE, ' ', 1, 16),
            new Token(Token::T_STRING, '"f\\"oo"', 1, 17, 1, 23),
            new Token(Token::T_SEMICOLON, ';', 1, 24),
            new Token(Token::T_WHITESPACE, ' ', 1, 25),
            new Token(Token::T_CLOSECURLY, '}', 1, 26),
        ], $tokens);
    }

    public function testEscape()
    {
        $tokens = (new Tokenizer())->tokenize(".\\31 a2b3c {\n\n }");

        $this->assertEquals([
            new Token(Token::T_WORD, '.', 1, 1, 1, 1),
            new Token(Token::T_WORD, '\\3', 1, 2, 1, 3),
            new Token(Token::T_WORD, '1', 1, 4, 1, 4),
            new Token(Token::T_WHITESPACE, ' ', 1, 5),
            new Token(Token::T_WORD, 'a2b3c', 1, 6, 1, 10),
            new Token(Token::T_WHITESPACE, ' ', 1, 11),
            new Token(Token::T_OPENCURLY, '{', 1, 12),
            new Token(Token::T_WHITESPACE, "\n\n ", 3, 0),
            new Token(Token::T_CLOSECURLY, '}', 3, 3),
        ], $tokens);
    }

    public function testBrackets()
    {
        $tokens = (new Tokenizer())->tokenize("(ab)");

        $this->assertEquals([
            new Token(Token::T_BRACKETS, '(ab)', 1, 1, 1, 4),
        ], $tokens);
    }

    public function testAtEnd()
    {
        $tokens = (new Tokenizer())->tokenize('@one{@two()@three""@four');

        $this->assertEquals([
            new Token(Token::T_ATWORD, '@one', 1, 1, 1, 4),
            new Token(Token::T_OPENCURLY, '{', 1, 5),
            new Token(Token::T_ATWORD, '@two', 1, 6, 1, 9),
            new Token(Token::T_OPENBRACKET, '(', 1, 10),
            new Token(Token::T_CLOSEBRACKET, ')', 1, 11),
            new Token(Token::T_ATWORD, '@three', 1, 12, 1, 17),
            new Token(Token::T_STRING, '""', 1, 18, 1, 19),
            new Token(Token::T_ATWORD, '@four', 1, 20, 1, 24),
        ], $tokens);
    }
}