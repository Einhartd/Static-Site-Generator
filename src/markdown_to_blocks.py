def markdown_to_blocks(markdown: str):
    extracted_blocks: list[str] = []
    
    extracted_blocks = markdown.split("\n\n")
    for i, block in enumerate(extracted_blocks):
        extracted_blocks[i] = extracted_blocks[i].strip()
        extracted_blocks[i] = extracted_blocks[i].lstrip("\n")
        if extracted_blocks[i] == "":
            extracted_blocks.remove("")
    
    return extracted_blocks
