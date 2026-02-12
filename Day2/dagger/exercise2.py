import dagger
import asyncio

async def main():
    async with dagger.Connection() as client:
        src = client.host().directory(".")

        container = (
            client.container()
            .from_("alpine")
            .with_directory("/src", src)
            .with_workdir("/src")
            .with_exec(["sh", "-c", "echo Mounted Successfully > result.txt"])
            .with_exec(["cat", "result.txt"])
        )

        print(await container.stdout())

asyncio.run(main())
