from pydantic import BaseModel, Field
from dotenv import load_dotenv
from agno.agent import Agent

from job_info import JOB_INFO

load_dotenv()


class JobData(BaseModel):
    title: str = Field(description="Título da vaga de emprego")
    company: str | None = Field(description="Nome da empresa, se disponível")
    location: str | None = Field(description="Localização da vaga, se disponível")
    description: str = Field(description="Descrição detalhada da vaga de emprego")
    requirements: list[str] | None = Field(
        description="Lista de requisitos para a vaga de emprego"
    )
    benefits: list[str] | None = Field(
        description="Lista de benefícios oferecidos pela vaga de emprego"
    )
    is_remote: bool = Field(description="Indica se a vaga é para trabalho remoto")


class JobAnalysis(BaseModel):
    seniority: str = Field(
        description="Nível de senioridade da vaga (ex: Júnior, Pleno, Sênior)"
    )
    technologies: list[str] = Field(
        description="Lista de tecnologias mencionadas na vaga"
    )
    english_required: bool = Field(
        description="Indica se o conhecimento de inglês é necessário para a vaga"
    )
    summary: str = Field(description="Resumo conciso da vaga de emprego")


job_parser_agent = Agent(
    name="JobParserAgent",
    description="Agente para extrair informações de vagas de emprego a partir de descrições textuais",
    output_schema=JobData,
    model="openai:gpt-4.1-mini",
)

job_analysis_agent = Agent(
    name="JobAnalysisAgent",
    description="Agente para analisar as informações extraídas de uma vaga de emprego e fornecer insights adicionais",
    output_schema=JobAnalysis,
    input_schema=JobData,
    model="openai:gpt-4.1-mini",
)

job_parser_result = job_parser_agent.run(JOB_INFO)

job_analysis_result = job_analysis_agent.run(job_parser_result.content)

print("=== Job Data ===")
print(job_parser_result.content.model_dump_json(indent=2))

print("\n=== Job Analysis ===")
print(job_analysis_result.content.model_dump_json(indent=2))
