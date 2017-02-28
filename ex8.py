formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
# If I put quotes on boolean values, they will work as string.
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# why it uses single-quote for some sentences and double-quatoes for other sentences?
# It is because %r is used for debugging. Python selects the most efficient way.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
