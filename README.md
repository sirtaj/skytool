
# Skytools WIP #

This is a set of tools for Skyrim modders and advanced users. This is very
much not release-worthy yet.

There are two parts to this project:


### SkyScraper Data Browser ###

With a lot of modding, the Skyrim install directory tends to fill up with
files and directories from multiple sources, such as mod installers like NMM
and custom changes made by the user. This GUI browser helps locate changed,
orphaned and missing files in the game install path and helps identify where
each one came from.

This bit is probably the most immediately useful bit of this project, but
still requires a lot of work. It uses PyQt for the GUI functionality.


### ESP/ESM Data Model ###

An easy pythonic object model for Skyrim ESP and ESM files. This includes
transparent read, write and safe modification. The model should also contain
enough reflection capability to allow code to generate views and transforms of
the model through metadata alone.

Since the most complete machine-parseable specification of the file format is
currently the RecordStructure.xml file shipped with TESVsnip, I'm using this
to generate the python model heuristically.

Once the model is complete, the plan is to analyze the subrecord structure to
identify common patterns and groups of subrecords. This will be used to
generate a better inheritance structure for records and to identify abstract
classes that are not immediately identifiable via the existing (mostly
reverse-engineered) file specifications.


## Intermediate Goal ##

Use the object model to allow easy creation of one-off modding operations such
as merging, splitting, cleaning, and automatic generation of records like
leveled lists and actors. With enough support from the python object model,
this should be relatively straightforward.


## Legal ##

Copyright Sirtaj Singh Kang, 2012 All code and artifacts currently released
under the terms of the LGPL.
