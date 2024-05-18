import asyncio
from pythonclient.FurnaceCheckBase import FurnaceCheckBase
from pythonclient.check_buffer import CheckBuffer


class TestCheck(FurnaceCheckBase):

    parameters ={ "bonjour" : "greeting"}
    @classmethod
    async def test(self):
        parameters = ["bonjour", "salut", 30]
        # await self.run(parameters, "bonjour", test="kwargs")
        print(parameters)

    # @FurnaceCheckBase.conform_command()
    @classmethod
    async def run(self, parameters =None):
        print("je suis dans le run de TestCheck")



if __name__ == "__main__":
    from pythonclient.utils.enums import CheckStatus


    parameters = ["bonjour", 30]
    check_buffer = CheckBuffer(*parameters)
    print(check_buffer)
    test = TestCheck("check", check_buffer)
    asyncio.run(test.run(parameters))


    print(f"test.parameters:{test.parameters}")
    print("end")

