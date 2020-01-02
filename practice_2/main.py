from practice_2.step import Step

if __name__ == "__main__":
    try:
        print(Step(2, 'five').make_step())
    except Exception as e:
        print(e)

    try:
        print(Step(0, 'five').make_step())
    except Exception as e:
        print(e)

    try:
        print(Step(2, 'ten').make_step())
    except Exception as e:
        print(e)