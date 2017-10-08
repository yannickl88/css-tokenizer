<?php
namespace Yannickl88\Component\CSS;

/**
 * @covers \Yannickl88\Component\CSS\Tokenizer
 */
class TokenizerTest extends \PHPUnit_Framework_TestCase
{
    public function testGetWhitespaces()
    {
        self::assertEquals([' ', "\n", "\t", "\r", "\f"], Tokenizer::getWhitespaces());
    }

    public function testWindowsLineEndings()
    {
        self::assertEquals([
            new Token(Token::T_WORD, 'foo', 1, 1, 1, 3),
            new Token(Token::T_SEMICOLON, ';', 1, 4),
            new Token(Token::T_WHITESPACE, "\r\n", 1, 5, 2, 0),
            new Token(Token::T_WORD, 'bar', 2, 1, 2, 3),
            new Token(Token::T_SEMICOLON, ';', 2, 4),
            new Token(Token::T_WHITESPACE, "\n  ", 2, 5, 3, 2),
        ], (new Tokenizer())->tokenize("foo;\r\nbar;\n  "));

        self::assertEquals([
            new Token(Token::T_WORD, 'foo', 1, 1, 1, 3),
            new Token(Token::T_WHITESPACE, ' ', 1, 4),
            new Token(Token::T_WORD, 'bar', 1, 5, 1, 7),
            new Token(Token::T_SEMICOLON, ';', 1, 8),
        ], (new Tokenizer())->tokenize('foo bar;'));

        self::assertEquals([
            new Token(Token::T_WORD, 'foo', 1, 1, 1, 3),
            new Token(Token::T_WHITESPACE, "\n\n", 1, 4, 3, 0),
            new Token(Token::T_WORD, 'bar', 3, 1, 3, 3),
            new Token(Token::T_SEMICOLON, ';', 3, 4),
        ], (new Tokenizer())->tokenize("foo\n\nbar;"));
    }

    /**
     * @dataProvider parseProvider
     */
    public function testParse($spec_file)
    {
        list($expected, $input) = SpecParser::getSpec(__DIR__ . '/spec/' . $spec_file);

        self::assertEquals($expected, (new Tokenizer())->tokenize($input), $spec_file);
    }

    public function parseProvider()
    {
        $base_dir = __DIR__ . '/spec/';
        $dir_iterator = new \RecursiveIteratorIterator(new \RecursiveDirectoryIterator($base_dir));

        /* @var \SplFileInfo $file */
        foreach ($dir_iterator as $file) {
            if (in_array($file->getFilename(),  ['.', '..'], true)) {
                continue;
            }
            if ($file->getExtension() !== 'spec') {
                continue;
            }

            yield [substr($file->getPathname(), strlen($base_dir))];
        }
    }
}
