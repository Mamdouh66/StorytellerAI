import storyteller
import utils


def main() -> None:
    writerGPT = storyteller.WriterGPT()
    critiqueGPT = storyteller.CritiqueGPT()

    init_story = writerGPT.generate_story()
    with open("../story_docs/init_story.md", "w") as f:
        f.write(init_story)

    prev_story = init_story
    for turn in range(3):
        critique = critiqueGPT.generate_critique(story=prev_story)
        with open(f"../story_docs/critique_{turn+1}.md", "w") as f:
            f.write(critique)

        story = writerGPT.generate_story(
            critique=critique, previous_story=prev_story, critique_turn=True
        )

        with open(f"../story_docs/story_after_critique_{turn+1}.md", "w") as f:
            f.write(story)

        prev_story = story

    utils.text_to_speech(text=story[:4000])


if __name__ == "__main__":
    main()
