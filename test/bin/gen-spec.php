<?php
require __DIR__ . '/../../vendor/autoload.php';

$input = '/* One hell of a block
style comment! */
@var: red;

// Get in line!
@var: white;';

$tokens = (new \Yannickl88\Component\CSS\Tokenizer())->tokenize($input);
$types = array_flip((new \ReflectionClass(\Yannickl88\Component\CSS\Token::class))->getConstants());

$output = $input . "\n============TEST\n";

foreach ($tokens as $token) {
    $output .= $types[$token->type] . ',';
    $output .= implode(':', $token->lines) . ',';
    $output .= implode(':', $token->offsets) . ',';
    $output .= json_encode($token->chars) . "\n";
}

echo $output;
