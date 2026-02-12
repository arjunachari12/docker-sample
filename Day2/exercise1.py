import dagger
import asyncio

async def main():
    async with dagger.Connection() as client:
        output = await (
            client.container()
            .from_("alpine")
            .with_exec(["echo", "Dagger in WSL working!"])
            .stdout()
        )
        print(output)

asyncio.run(main())
