def two_fer(name: str = '') -> str:
    return f"One for {name if name != '' else 'you'}, one for me."


if __name__ == '__main__':
    print(two_fer('Max'))
    print(two_fer(''))
