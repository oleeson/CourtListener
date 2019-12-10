Utils folders just carry scripts/methods/etc that might be useful
**at the current level or downstream only**

For example, here at the src level (the highest level we'll even consider having scripts),
we might include very general code that might be used in both data_cleaning and data_downloading.

At lower levels, say in the "data_cleaning" folder, we might have a "utils" folder that
includes common code/functionality that is more specific to that portion of our pipeline.
Where possible, we'll be extending code (ie. inheriting from a base class
that exists in /FLPResearch/src/utils/, meaning we import that code from "upstream")
but when needed can write as much "data_cleaning"-specific code as we need.

We really try to avoid importing anything from lower in the directory structure.
If we find we *are* importing from lower in the directory, we likely need to promote
that we're importing to a higher level, and extend it back to the lower level.