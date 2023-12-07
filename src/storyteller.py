import instructor

from openai import OpenAI
from config import settings


class WriterGPT:
    def __init__(self):
        self.client = OpenAI(api_key=settings.API_KEY)

    def generate_story(
        self,
        critique: str | None,
        character: str | None,
        world_building: str | None,
        previous_story: str | None,
        critique_turn: bool = False,
    ) -> str:
        response = self.client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                self.prompt_template(
                    self,
                    critique=critique,
                    character=character,
                    world_building=world_building,
                    previous_story=previous_story,
                    critique_turn=critique_turn,
                )
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content

    def prompt_template(
        self,
        critique: str,
        character: str,
        world_building: str,
        previous_story: str,
        critique_turn: bool = False,
    ) -> str:
        if critique_turn:
            after_critquie_prompt = f"""
            Based on the critique and suggestions provided, revise and enhance the high fantasy story.
            Focus on addressing the identified areas of improvement in narrative structure, character development,
            and world-building. Incorporate the suggested changes to enhance plot coherence, deepen character arcs,
            and enrich the descriptive elements of the fantasy world. Ensure the story maintains a balanced flow,
            with improved dialogue, action, and descriptive passages. Pay particular attention to refining the emotional depth 
            and thematic resonance of the narrative. Work on crafting a more engaging and immersive storytelling experience that
            captivates the reader from beginning to end.

            critique: {critique}

            character: {character}

            world-building: {world_building}

            keep in mind this is your previous writing: {previous_story}
            """
            return after_critquie_prompt

        init_story_prompt = f"""
        Write a compelling high fantasy story based with the title {settings.STORY_TITLE} and with the following description
        {settings.STORY_DESCRIPTION} focus on the initial plot and character outlines provided.
        Focus on creating a multi-layered narrative with detailed descriptions, complex characters, and an engaging plot structure.
        Ensure the story unfolds with a captivating introduction, develops tension and conflict in the middle, and concludes
        with a satisfying climax. Pay attention to crafting vivid scenes that bring the fantasy world to life, highlighting
        its unique elements, landscapes, and creatures. write 4000 tokens.
        """
        return init_story_prompt


class CritiqueGPT:
    ...


class CharacterGPT:
    ...


class WorldGPT:
    ...
