def markdown_to_blocks(markdown: str) -> list[str]:
    extracted_blocks: list[str] = []

    raw_blocks = markdown.split("\n\n")

    for block in raw_blocks:
        lines = block.split("\n")
        cleaned_lines = [line.strip() for line in lines]
        cleaned_block = "\n".join(cleaned_lines).strip()
        if cleaned_block:
            extracted_blocks.append(cleaned_block)
    
    return extracted_blocks
