import dagger
import asyncio

async def main():
    async with dagger.Connection() as client:

        step1 = (
            client.container()
            .from_("alpine")
            .with_exec(["sh", "-c", "echo Multi Step Workflow > output.txt"])
        )

        step2 = step1.with_exec(["cat", "output.txt"])

        print(await step2.stdout())

asyncio.run(main())
