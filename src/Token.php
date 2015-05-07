<?php
namespace Yannickl88\Component\CSS;

/**
 * @author Yannick de Lange <yannick.l.88@gmail.com>
 */
class Token
{
    const T_WHITESPACE   = 0;
    const T_BRACKETS     = 1;
    const T_OPENBRACKET  = 2;
    const T_CLOSEBRACKET = 3;
    const T_STRING       = 4;
    const T_WORD         = 5;
    const T_ATWORD       = 6;
    const T_COMMENT      = 7;

    public $type;
    public $chars;
    public $lines   = [];
    public $offsets = [];

    /**
     * @param string $type
     * @param string $chars
     * @param int $line
     * @param int $offset
     * @param int $line_end
     * @param int $offset_end
     */
    public function __construct($type, $chars, $line, $offset, $line_end = -1, $offset_end = -1)
    {
        $this->type      = $type;
        $this->chars     = $chars;
        $this->lines[]   = $line;
        $this->offsets[] = $offset;

        if ($line_end >= 0) {
            $this->lines[] = $line_end;
        }
        if ($offset_end >= 0) {
            $this->offsets[] = $offset_end;
        }
    }
}
