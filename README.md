ZPL generation and rendering tools
----------------------------------

This is a collection of tools to help render images to and from ZPL.

Rendering ZPL to Image
======================

To (very badly) render (a small subset of) ZPL to an image, run

    ./pyzplr <zplfile>

and it will create a file with the same name as "zplfile" but with a
".png" suffix.

Rendering and Image to ZPL
==========================

You can use the `render_test_image_to_zpl` script with a PNG as the
argument to render a PNG to a test ZPL file. The you can use the
intermediary file suffixed with ".dg" for other ZPL files.

The basic process takes the PNG to a hex-encoded black-and-white image -- 
each bit represents a single pixel. The hex data is then encoded with
a run-length compression algorithm (as specified in the ZPL Programming
Guide). From there, you need to take that and insert a 

Other resources
===============

* [ZPL II Programming Guide Volume One](https://www.zebra.com/content/dam/zebra/manuals/printers/common/programming/zplii-pm-vol1.pdf)
* [ZPL II Programming Guide](https://www.servopack.de/support/zebra/ZPLII-Prog.pdf)
* [Labelary](http://labelary.com/) - A much, much, much better render.  Not F/OSS.
