
    GIL（Global Interpreter Lock）：全局解释器锁：


    是计算机程序设计语言解释器用于同步线程的一种机制，它使得任何时刻仅有一个线程在执行。
    即便在多核心处理器上，使用 GIL 的解释器也只允许同一时间执行一个线程。


    python自带的解释器是Cpython。Cpython解释器的多线程实际上是假的多线程
    (在多核CPU中，只能利用一核，不能利用多核)。同一时刻只有一个线程在执行，
    为了保证同一时刻只有一个线程执行，在Cpython中有一个东西叫做GIL(全局解释器锁)
    这个解释器锁是有必要的，因为Cpython解释器的内存管理不是线程安全的。


    除了Cpython解释器，在python中还有其他解释器，这些没有GIL：
        1、Jypython：用Java实现的python解释器，不存在GIL锁；
        2、IronPython：用.NET实现的Python解释器，不存在GIL锁；
        3、PyPy：用Python实现的Python解释器，存在GIL；
    GIL虽然是一个假的多线程。但是在处理一些I/O操作还是可以在很大程度上提高效率。
    在I/O操作上建议使用多线程提高效率。在一些CPU计算操作上不建议使用多线程，而建议使用多进程








