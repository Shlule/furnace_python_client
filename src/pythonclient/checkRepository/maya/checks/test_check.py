import asyncio
from pythonclient.FurnaceCheckBase import FurnaceCheckBase
from check_buffer import CheckBuffer


class TestCheck(FurnaceCheckBase):

    parameters ={ "bonjour" : "greeting"}

    async def test(self):
        parameters = ["bonjour", "salut", 30]
        await self.run(parameters, "bonjour", test="kwargs")
        print("test")

    @FurnaceCheckBase.conform_command()
    async def run(self, parameters):
        print("je suis dans le run de TestCheck")



if __name__ == "__main__":
    from pythonclient.utils.enums import CheckStatus

    dict_parameters = {"name": "bonjour",
                       "status": 1}
    parameters = ["bonjour", "salut", 30]
    check_buffer = CheckBuffer(**dict_parameters)
    print(check_buffer)
    test = TestCheck("check", check_buffer)
    asyncio.run(test.run(parameters))


    print(f"test.parameters:{test.parameters}")
    print("end")

