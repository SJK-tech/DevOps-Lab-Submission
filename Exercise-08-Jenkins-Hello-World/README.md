# Exercise 8: Hello World Jenkins Job

## Objective
Create and execute a Jenkins Freestyle job that retrieves a shell script from GitHub and runs it.

## GitHub Repository
`https://github.com/SJK-tech/devops-sample-code`

## Script
The repository contains `hello-world.sh`:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

## Jenkins Configuration
- Job name: `HelloWorld`
- Job type: Freestyle project
- Source Code Management: Git
- Repository: `https://github.com/SJK-tech/devops-sample-code.git`
- Branch: `*/main`
- Build step: Execute shell
- Command: `sh hello-world.sh`

## Execution
The job was built using **Build Now**. The Console Output confirmed the script ran successfully.

## Result
The job printed `Hello, Jenkins!` and completed with `Finished: SUCCESS`.
