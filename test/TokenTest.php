<?php
namespace Yannickl88\Component\CSS;

/**
 * @covers \Yannickl88\Component\CSS\Token
 */
class TokenTest extends \PHPUnit_Framework_TestCase
{
    public function testConstructor()
    {
        $token = new Token(Token::T_CLOSEBRACKET, 'foo', 42, 13, 1337, 43);

        self::assertEquals(Token::T_CLOSEBRACKET, $token->type);
        self::assertEquals('foo', $token->chars);
        self::assertEquals([42, 1337], $token->lines);
        self::assertEquals([13, 43], $token->offsets);
    }
}
