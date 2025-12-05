#!/bin/bash
set -e

# نص التعليمات المرسل للنموذج

prompt="Role: Minecraft Localization Expert.
Task: Translate the values in the attached file into Arabic strictly.

Constraints:
1. Preserve all Key IDs exactly. Only translate the string values.
2. IMPORTANT: Do NOT touch formatting codes (e.g., §a, §l) or placeholders (e.g., %s, %1$s). Keep them exact.
3. Process the entire file in one go. Do not skip lines.
4. Output: Edit the file directly/provide the full code block. No conversational text.
5. Use official Minecraft Arabic terminology.

Execute the translation on the full file now."
echo "🔥 بدء التعريب باستخدام Auto-Edit..."
echo

echo "➡️  تعريب: $1"
    
gemini -m "gemini-2.5-flash" --approval-mode "auto_edit" -p "$prompt قم الآن بتعريب الملف: $1"

