<?php

require __DIR__ . '/../../vendor/autoload.php';

$base_dir = __DIR__ . '/../spec/';
$dir_iterator = new \RecursiveIteratorIterator(new \RecursiveDirectoryIterator($base_dir));

/* @var \SplFileInfo $file */
foreach ($dir_iterator as $file) {
    if (in_array($file->getFilename(), ['.', '..'], true)) {
        continue;
    }

    if ($file->getExtension() !== 'spec') {
        continue;
    }

    list($expected, $input) = Yannickl88\Component\CSS\SpecParser::getSpec($file);

    $tokens = (new \Yannickl88\Component\CSS\Tokenizer())->tokenize($input);
    $types = array_flip((new \ReflectionClass(\Yannickl88\Component\CSS\Token::class))->getConstants());

    $output = $input . "\n============TEST\n";

    foreach ($tokens as $token) {
        $output .= $types[$token->type] . ',';
        $output .= implode(':', $token->lines) . ',';
        $output .= implode(':', $token->offsets) . ',';
        $output .= json_encode($token->chars) . "\n";
    }

    echo 'UPDATING: ', $file, "\n";

    file_put_contents($file, $output);
}
