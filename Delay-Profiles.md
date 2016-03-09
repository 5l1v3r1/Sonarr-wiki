## _(Settings -> Profiles -> Delay Profiles)_

Delay profiles allow you to reduce the number of releases that will be downloaded for an episode, by adding a delay  while Sonarr will continue to watch for releases that better match your preferences. 

For example, some shows will receive half a dozen different releases of varying quality in the hours after an episode airs, and without delay profiles Sonarr might try to download all of them. With delay profiles, Sonarr can be configured to ignore the first few hours of releases.

Delay profiles are also helpful if you want to emphasize one protocol (Usenet or BitTorrent) over the other. ([See Example 3](#example-3))

#### How Delay Profiles Work

The timer begins as soon as Sonarr detects an episode has a release available. This release will show up in your Queue with a clock icon to indicate that it is under a delay.

During the delay period, any new releases that become available will be noted by Sonarr. When the delay timer expires, Sonarr will download the single release which best matches your quality preferences.

The timer period can be different for Usenet and Torrents. Each profile can be associated with one or more tags to allow you to customize which shows have which profiles. A delay profile with no tag is considered the default and applies to all shows that do not have a specific tag.

#### Examples

For each example, assume the user has the follow quality profile active:
* **HDTV 720p** and above are allowed
* **WebDL 720p** is the quality cutoff
* **WebDL 1080p** is the highest ranked quality

##### Example 1:

In this simple example, the profile is set with a 120 minute (two hour) delay for both Usenet and Torrent.

At `11:00pm` the first release for an episode is detected by Sonarr and the 120 minute clock begins. At `1:00am`, Sonarr will evaluate any releases it has found in the past two hours, and download the best one, which is **HDTV 720p**.

At `3:00am` another release is found, which is **WebDL 720p**. Another 120 minute clock begins. At `5:00am` the best-available release is downloaded. Since the cutoff is now reached, the episode no longer monitored and Sonarr will stop looking for new releases.

At any point, if a **WebDL 1080p** release is found, it will be downloaded immediately because it is the highest-ranking quality. If there is a delay timer currently active it will be cancelled.

##### Example 2:

This example has different timers for Usenet and Torrents. Assume a 120 minute timer for Usenet and a 180 minute timer for BitTorrent.

At `11:00pm` the first release for an episode is detected by Sonarr and both timers begin. At `1:00am`, Sonarr will evaluate any releases, and if there are any acceptable **Usenet** releases, the best one will be downloaded and both timers will end. If not, Sonarr will wait until `2:00am` and download the best release, regardless of which source it came from.


##### Example 3:

A common use for delay profiles is to emphasize one protocol over another. For example, you might only want to download a BitTorrent release if nothing has been uploaded to Usenet after a certain amount of time.

You could set a 60 minute timer for BitTorrent, and a 0 minute timer for Usenet.

If the first release that is detected is from Usenet, Sonarr will download it immediately.

If the first release is from BitTorrent, Sonarr will set a 60 minute timer. If any qualifying Usenet release is detected during that timer, the BitTorrent release will be ignored and the Usenet release will be grabbed.


