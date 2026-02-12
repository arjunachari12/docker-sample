import dagger
import asyncio

async def main():
    async with dagger.Connection() as client:

        # Simulated AI-generated code
        code = 'print("AI Generated Code Executed Safely Inside Container")'

        container = (
            client.container()
            .from_("python:3.11-alpine")
            .with_new_file("/app/script.py", code)
            .with_exec(["python", "/app/script.py"])
        )

        print(await container.stdout())

asyncio.run(main())
