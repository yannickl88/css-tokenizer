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

    /**
     * @dataProvider parseProvider
     */
    public function testParse($spec_file)
    {
        list($expected, $input) = SpecParser::getSpec($spec_file);

        self::assertEquals($expected, (new Tokenizer())->tokenize($input));
    }

    public function parseProvider()
    {
        return [
            [__DIR__ . '/spec/css/basic.css.spec'],
            [__DIR__ . '/spec/css/url.css.spec'],
            [__DIR__ . '/spec/css/media-query.css.spec'],
            [__DIR__ . '/spec/css/comment.css.spec'],
            [__DIR__ . '/spec/css/comment-multiline.css.spec'],
            [__DIR__ . '/spec/css/string.css.spec'],
            [__DIR__ . '/spec/css/escape.css.spec'],
            [__DIR__ . '/spec/css/brackets.css.spec'],
            [__DIR__ . '/spec/css/at-end.css.spec'],
        ];
    }
}
