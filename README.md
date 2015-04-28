# custombase64
Custom Base64 encoder/decoder

A lot of malware use base64 encoding for C2 communication or just to simply obfuscate their code.
Most of the time, the bad guys use a custom charset. This is a problem since there really is no way
that I know of to efficiently brute force the charset that was used.
But if you can peek into the executable that is performing the encoding, you may find the charset used.

There are tools out there from people like <a href="http://www.kahusecurity.com/">Kahu Security</a> that can decode using custom charsets.
For decoding a couple hundred bytes of encoded data, that tool is great.
But for large files >= 1 MB I have witnessed etreme slowness. So another excuse to code up some python. :)

