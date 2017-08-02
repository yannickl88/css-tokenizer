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
