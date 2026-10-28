# Didge Archive

An open collection of didgeridoos: their inner shape, how they sound, and the files to build them yourself.

Didge Archive is part of the [Didgitaldoo](https://didgitaldoo.github.io/) project.

## What is this?

A didgeridoo is basically a long, hollow tube. Its sound is determined almost entirely by the shape of the inside: how wide the tube is at every point along its length. Two didgeridoos that look similar from the outside can sound completely different.

The Didge Archive documents real, playable didgeridoos together with everything you need to study or recreate them:

- **The shape** of the bore (the inner diameter along the whole length)
- **Sound recordings** of the instrument being played
- **3D files** (STL and Blender) so the didgeridoo can be 3D printed
- **Photos and a short description**

I started this collection to evaluate my own work on [DidgeLab](https://github.com/Didgitaldoo/didge-lab), a toolkit for simulating and designing didgeridoos with computers. To know whether a simulated didgeridoo is any good, I need real instruments to compare against: measured shapes and real recordings. The archive is that ground truth, and I'm publishing it so others can use it too.

### Who is it for?

- **Didgeridoo makers** who want proven shapes as a starting point
- **Players** who want to hear an instrument before building it
- **Researchers and developers** working on acoustics, simulation, optimisation or machine learning for instrument design
- **Anyone curious** about what makes a didgeridoo sound the way it does

## The didgeridoos

| Name | Shape | Notes |
| --- | --- | --- |
| Malveira | straight | F#, modelled after a didgeridoo seen online |
| Arusha | saxodidge | |
| Nazare | straight | |
| Kizimkazi | straight | |
| Tamaki1, Tamaki2 | straight | |
| Matema | straight | |
| Open Didgeridoo | saxodidge | D, built after the [Open Didgeridoo](https://www.windproject.it/open-didgeridoo/) by Andrea Ferroni |
| Open Didgeridoo Straight | straight | Straight version of the Open Didgeridoo |

A *straight* didgeridoo is a single tube. A *saxodidge* is bent back on itself, like a saxophone, which makes long instruments easier to hold and play.

Some entries are also on Thingiverse for easy printing, see the `thingiverse` field in the index.

## Repository layout

```
didge-archive.json   index of all didgeridoos, links everything together
geometries/          bore shape of each didgeridoo (JSON)
audio-samples/       WAV recordings
stl-files/           3D printable models (zipped STL)
blender-files/       Blender source files (zipped)
images/              photos
scripts/             helper scripts
```

### The index: `didge-archive.json`

This is the entry point. It is a list with one object per didgeridoo:

```json
{
    "name": "Malveira",
    "creator": "Jan Nehring",
    "uploader": "Jan Nehring",
    "shape": "straight",
    "geometry": "geometries/malveira.json",
    "audio-samples": {
        "hand-open": "audio-samples/malverira-hand1.wav",
        "hand-closed": "audio-samples/malveira-hand2.wav",
        "neutral-sound": "audio-samples/malveira-neutral-sound.wav",
        "song": "audio-samples/malveira-short-song.wav"
    },
    "stl-files": ["stl-files/malveira.stl.zip"],
    "blender-files": ["blender-files/malveira.blend.zip"],
    "images": ["images/malveira.png"],
    "description": "...",
    "license": "...",
    "thingiverse": "https://www.thingiverse.com/thing:7014414"
}
```

`creator` is the person who designed the didgeridoo, `uploader` is the person who added it to the archive. They are often the same person, but not always (the Open Didgeridoo was designed by Andrea Ferroni). Please fill in both when you contribute.

All paths are relative to the repository root. Not every field is present for every entry.

### Geometry files

A geometry file is a JSON list of `[position, diameter]` points, in millimetres. `position` is the distance from the mouthpiece, `diameter` is the inner diameter at that point. Connecting the points with straight lines gives the bore of the didgeridoo.

```json
[[0, 32], [44.75, 30.90], [49.58, 31.17], ...]
```

This format is what DidgeLab reads and writes, so you can load an archive geometry there directly.

### Audio samples

Each didgeridoo is recorded in several ways, where available:

| Key | What it is |
| --- | --- |
| `neutral-sound` | The plain, sustained drone |
| `hand-open` / `hand-closed` | The same drone with the hand at the bell open or closed, to show how the sound changes |
| `song` | A short piece played on the instrument |

Recordings are WAV files. The Open Didgeridoo Straight entry has only a short and a long sample.

## License

The data in this archive is licensed under
[**Creative Commons BY-NC-SA 4.0**](LICENSE). You may copy, share and adapt it, as long as you:

- **give credit** (see [Citing](#citing)),
- **do not use it commercially** (NonCommercial), and
- **share adaptations under the same license** (ShareAlike).

For commercial use, please get in touch.

**Exceptions:** the Open Didgeridoo entries are based on a design by Andrea Ferroni and stay under the [Open Didgeridoo License](https://www.windproject.it/open-didgeridoo/). Please check its terms before using these entries.

## Contributing

Contributions are very welcome. The archive is more useful the more instruments it contains, and I'd love to see shapes and sounds from other makers and players.

You can contribute a new didgeridoo, or improve an existing entry (better recordings, missing files, corrections).

**How to add a didgeridoo:**

1. Fork this repository.
2. Add your files:
   - a geometry file in `geometries/` (required)
   - audio samples in `audio-samples/` (strongly recommended, at least `neutral-sound`)
   - STL files, Blender files and images if you have them
3. Add an entry for your didgeridoo to `didge-archive.json`, following the structure above.
4. Check that every path in your entry points to an existing file.
5. Open a pull request and briefly describe the instrument (key, material, how it was built or measured).

**Please make sure that:**

- you made the recordings and files yourself, or have the right to share them
- you are happy to release your contribution under CC BY-NC-SA 4.0, since all data in this repository shares the same license; by opening a pull request you agree to this
- your recordings contain only the didgeridoo (no music or voices of other people)
- file names are lowercase and use hyphens, like the existing ones

If you're not sure about something, open an issue and ask.

## Citing

If you use the archive in research, please cite this repository like a website, with Jan Nehring as the author. A citation is not required by the license but helps others find it.

> Nehring, Jan. *Didge Archive*. 2026. https://github.com/Didgitaldoo/didge-archive (accessed DD Month YYYY).

Adjust the year and access date, and the format to your citation style.

## Related

- [DidgeLab](https://github.com/Didgitaldoo/didge-lab), design and simulate didgeridoos with code
