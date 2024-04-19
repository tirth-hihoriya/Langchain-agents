from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.agents import load_tools, initialize_agent, AgentType

load_dotenv()

def generate_pet_name(animal_type, petcolor):
    llm = OpenAI(temperature=0.7)
    prompt_template_name = PromptTemplate(
        input_variables = ['animal_type', 'petcolor'],
        template = f'I have a {animal_type} pet and I want a cool namw for it, it is {petcolor} in color. Suggest me five cool names for my pet'
    )

    name_chain  = LLMChain(llm = llm, prompt  = prompt_template_name, output_key='pet_name')
    responce = name_chain({'animal_type': animal_type, 'petcolor': petcolor})
    return responce

def langchain_agent():
    llm = OpenAI(temperature=0.5)
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    result = agent.run("What is average age of dog;using wikipedia? Multiply the age by 3.")
    print(result)
    

if __name__ == '__main__':
    langchain_agent()
    # print(generate_pet_name('cat', 'red'))