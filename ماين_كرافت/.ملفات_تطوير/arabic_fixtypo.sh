#!/bin/bash
set -e

# نص التعليمات المعدل: يركز على التدقيق والتصحيح

prompt="Role: Minecraft Localization QA Specialist.
Task: Proofread and correct the Arabic translations in the provided file.

Instructions:
1. Analyze the existing Arabic text for grammar, spelling, or contextual errors.
2. Fix any translations that are inaccurate or inconsistent with official Minecraft terminology.
3. Constraints:
   - Preserve all Key IDs exactly.
   - CRITICAL: Do NOT modify formatting codes (e.g., §a, §l, &c) or placeholders (e.g., %s, %1$s, {0}). Keep them exact and ensure they are placed correctly within the Arabic sentence structure.
   - If a line is already correct, keep it as is.
4. Output: Return the full corrected file content directly. No conversational text.

Execute the correction on the full file now."

echo "🔥 بدء فحص وتصحيح الأخطاء في التعريب..."
echo

echo "➡️  جاري تدقيق: $1"

# ملاحظة: تأكد من إصدار الموديل، عادة المتوفر هو gemini-1.5-flash
# تم تعديل الرسالة المرسلة للنموذج لتتوافق مع البرومت الجديد
gemini -m "gemini-2.5-flash" --approval-mode "auto_edit" -p "$prompt قم بمراجعة وتصحيح أخطاء الملف: $1"
