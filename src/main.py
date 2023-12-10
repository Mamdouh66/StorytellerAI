import storyteller
import utils


def main() -> None:
    writerGPT = storyteller.WriterGPT()
    critiqueGPT = storyteller.CritiqueGPT()
    characterGPT = storyteller.CharacterGPT()
    worldGPT = storyteller.WorldGPT()
    
    init_world = worldGPT.generate_world()
    init_characters = characterGPT.generate_characters()

    init_story = writerGPT.generate_story(
        character=init_characters, world_building=init_world
    )
    with open("./story_docs/init_story.md", "w") as f:
        f.write(init_story)

    prev_story = init_story
    for turn in range(3):
        critique = critiqueGPT.generate_critique(story=prev_story)
        with open(f"./story_docs/critique_{turn+1}.md", "w") as f:
            f.write(critique)

        story = writerGPT.generate_story(
            critique=critique, previous_story=prev_story, critique_turn=True
        )
        with open(f"./story_docs/story_after_critique_{turn+1}.md", "w") as f:
            f.write(story)

        prev_story = story

    image_url = utils.generate_image(text=story)
    with open("./story_docs/final_story.md", "w") as f:
        f.write(f"![Chapter Story]({image_url})  <br> {story}")

    utils.text_to_speech(text=story[:4000])


if __name__ == "__main__":
    main()
