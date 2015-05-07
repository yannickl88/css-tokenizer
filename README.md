# CSS Tokenizer
PHP implementation of a CSS tokenizer. This implementation was heavily inspired by the javascript variant that was developed by https://github.com/postcss/postcss. However, the result is slightly different.

## Usage
Usage of the tokenizer is pretty straight forward:
```php
<?php
use Yannickl88\Component\CSS\Tokenizer;

$tokens = (new Tokenizer())->tokenize('span { padding: 2px; margin: 2px; }');
```
This is equivalent to:
```php
$tokens = [
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
];
```
What you do next is entirely up to you!

## Token types
If you have a token, you can access some public properties:
```php
$token->type; // for the type
$token->chars; // for the characters
$token->lines; // array containing start and (sometimes) end line
$token->offsets; // array containing start and (sometimes) end offset
```
> Note: Only tokens which can span multiple lines will have a second value in the `lines` and `offsets` field. These are `T_WORD`, `T_WHITESPACE`, `T_STRING`, `T_ADWORD`, and `T_COMMENT`.

The following types are defined:
 * `T_WHITESPACE`, white space characters like ` `, `\t`, `\n`, `\r` and `\f`.
 * `T_WORD`, all words, like `color`, `padding-top` or `12px`.
 * `T_COLON`, colon `:`.
 * `T_SEMICOLON`, semi-colon `;`.
 * `T_STRING`, everything between `'` or `"` quotes, like `"/path/to/my/image.jpg"`.
 * `T_OPENBRACKET`, open bracket `(`.
 * `T_CLOSEBRACKET`, close bracket `)`.
 * `T_OPENCURLY`, open curly bracket `{`.
 * `T_CLOSECURLY`, close curly bracket `}`
 * `T_ATWORD`, all words that start with a `@`, like `@media` or `@font-face`.
 * `T_COMMENT`, comments, like `/* comment */`.
 
> Note: There is also `T_BRACKETS`, however this is only in case of parse errors that you will see this token.

## Installation
Installing is pretty easy, this package is available on [packagist](https://packagist.org/packages/ydelange/css-tokenizer).
```
$ composer require yannickl88/css-tokenizer
```
Or you can add this to your composer.json manually:
```javascript
"require" : {
    "yannickl88/css-tokenizer" : "*@dev-master"
}
```
> Note: You can use dev-master if you want the latest changes, but this is not recommended for production code!
