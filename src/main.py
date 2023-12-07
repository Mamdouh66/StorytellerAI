import storyteller


def main():
    writerGPT = storyteller.WriterGPT()
    critiqueGPT = storyteller.CritiqueGPT()

    init_story = writerGPT.generate_story()
    with open("init_story.md", "w") as f:
        f.write(init_story)

    story = init_story
    for i in range(2):
        critique = critiqueGPT.generate_critique(story=init_story)
        with open(f"critique_{i}.md", "w") as f:
            f.write(critique)

        story = writerGPT.generate_story(
            critique=critique, previous_story=init_story, critique_turn=True
        )

        with open(f"story_after_critique_{i}.md", "w") as f:
            f.write(story)


if __name__ == "__main__":
    main()
