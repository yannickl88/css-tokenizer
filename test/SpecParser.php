<?php
namespace Yannickl88\Component\CSS;

/**
 * Simple parser for the .spec files.
 */
final class SpecParser
{
    public static function getSpec($file)
    {
        $types = (new \ReflectionClass(Token::class))->getConstants();

        $input = '';
        $expected = [];
        $eof = false;

        foreach (file($file) as $line) {
            if (1 === preg_match('/^===+TEST$/', trim($line))) {
                $eof = true;
                continue;
            }

            if ($eof) {
                if (empty($line)) {
                    continue;
                }

                $parts = explode(',', $line, 4);

                $type = $types[$parts[0]];
                $lines = explode(':', $parts[1]);
                $offsets = explode(':', $parts[2]);
                $chars = json_decode($parts[3]);

                $expected[] = new Token(
                    $type,
                    $chars,
                    (int) $lines[0],
                    (int) $offsets[0],
                    isset($lines[1]) ? (int) $lines[1] : -1,
                    isset($offsets[1]) ? (int) $offsets[1] : -1
                );
            } else {
                $input .= $line;
            }
        }

        return [$expected, trim($input)];
    }
}
