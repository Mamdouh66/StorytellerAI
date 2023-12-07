import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_KEY: str = os.getenv("OPENAI_API_KEY")
    # MODEL_NAME: str = "gpt-4-1106-preview"
    MODEL_NAME: str = "gpt-3.5-turbo"

    STORY_TITLE: str = "Sagas of Mythranor"
    STORY_DESCRIPTION: str = """
    In the enchanting world of Mythranor, a realm steeped in ancient magic and inhabited by diverse and mythical beings,
    an epic narrative begins to unfold. This high fantasy world, comprised of four grand empires, has known an age of peace 
    and harmony, overseen by the Celestial Sages, powerful beings who are custodians of the world's equilibrium and guardians 
    of the mystical elements.
    Darkness rises in the East as a once-banished warlock, known as Zarethor, re-emerges with the lost art of Dark Ether, 
    threatening to disrupt the world's harmony. His emergence marks the beginning of an era of strife, propelling Mythranor
    towards the brink of destruction.
    At the heart of this saga is a young human heroine, Seraphina, a warrior with a destiny entwined with the future of Mythranor.
    Propelled by an ancient prophecy, she embarks on a quest to unite the diverse inhabitants of Mythranor - the Skyborne Elves,
    the subterranean Forge Dwarves, the mystical Merfolk of the Azure Depths, and the arcane Phoenix Touched.
    Joining Seraphina is a motley crew of brave souls: Eolan, an Elf archer with a secret burden; Brom, a jovial Dwarf with
    unmatched prowess in battle; Lysandra, a Merfolk sorceress whose magic is as unpredictable as the seas; and Orion, a Phoenix 
    Touched with the power to harness the flames of rebirth.
    Their mission is to recover the Celestial Crystals, ancient and powerful relics of the Celestial Sages, scattered across the 
    furthest reaches of Mythranor, each protected by formidable trials that challenge their bonds and beliefs.
    In their journey, they traverse through mythical landscapes, encounter legendary beasts like the shadowy Wraith Dragons and
    the noble Griffins of the Sunspire Mountains. They face inner demons and external foes, all the while forging a bond that
    transcends their differences.
    """

    class Config:
        env_file = ".env"


settings = Settings()
