function fibonacci(num) {
  if (num === 1) {
    return 0;
  }
  if (num === 2) {
    return 1;
  }
  var prepre = 0;
  var pre = 1;
  var fib;
  for (i = 2; i < num; i++) {
    fib = pre + prepre;
    prepre = pre;
    pre = fib;
  }
  return fib;
}
