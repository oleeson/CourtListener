The data folder stores... well, data. Pretty straightforward, but we'll establish some
conventions that make storing, tracking, and retrieving data much easier.

1. Raw data goes in its own folder, as it was when obtained from its source,
    and stays untouched, ideally forever.
2. Intermediate datasets should be destroyed and rebuilt and each full run of our pipeline.
    This ensures that data preparation scripts aren't accidentally pulling from old tables,
    decreasing the chance that our pipeline actually breaks.
3. We name the intermediate datasets descriptively, and number them according to the scripts which produce them.
    This makes "data lineage" much easier, and, if anything breaks, we know exactly which script to look at.
    Eg. a script called "remove_phone_numbers_010.py" will create the dataset "data_without_phone_numbers_010.csv".
    We might name the next script in our pipeline "remove_addresses_020.py", and the
    corresponding dataset "data_without_personal_info_020.json"
        (we use conventions like _010 -> _020 to account for the possibility
        of needing to introduce another intermediate step, eg. _015)
4. We log as much as we can, especially timestamps for when data was sourced or built, etc.