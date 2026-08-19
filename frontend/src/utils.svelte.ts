type APIdata = {
	[genre: string]: Video[];
}

export type Video = {
	title: string;
	channel_name: string;
	description: string;
	published_at: string;
	thumbnail_link: string;
	liked: boolean;
	tags: string[];
	id: string;
	duration: string;
	category: string;
	view_count: string;
	watched: boolean;
	genre: string;
}

export function count(data: APIdata): [string[], number, Video[][]] {
	const genres = Object.keys(data);
	const videos = Object.values(data);
	let videoCount: number = 0;

	for (let i = 0; i < videos.length; i++) {
		const genreVideos: Video[] = videos[i];
		for (let j = 0; j < genreVideos.length; j++) {
			videoCount += 1
		}
	}
	return [genres, videoCount, videos];
}

export function formatISO(duration: string): string {
	/*
		* Formats a string of the type PT11H35M12S
		* The first two chracters are always going to be 'PT'
		* I have two choices here - use regex or use the Temporatl.Duration and Intl.DurationFormat API which are not baseline yet on MDN
		* eh, who cares it's the safari guys who are going to be affected by this - I don't care about them
		* their fault for not using helium (literally the best browser ever made)
		* wait no this Temporal thing it's not even in Typescript yet.
		* Hmm, regex might be it.
	*/
	const reHours= /(\d+)H/
	const reMins = /(\d+)M/
	const reSecs = /(\d+)S/
	const oneDigit = [1, 2, 3, 4, 5, 6, 7, 8, 9];
	let returnable: string = '';
	let hours, minutes, seconds;

	let hoursMatch = duration.match(reHours);
	let minsMatch = duration.match(reMins);
	let secsMatch = duration.match(reSecs);

	if (hoursMatch) {
		// this means that this is not null and hours exists.
		hours = hoursMatch[1];
		if (oneDigit.includes(Number(hours))) hours = `0${hours}`
		returnable += `${hours}:`;
	}

	if (minsMatch) {
		minutes = minsMatch[1];
		if (oneDigit.includes(Number(minutes))) minutes = `0${minutes}`
		if (returnable.indexOf(':') !== -1) returnable += `${minutes}:` // means that we already have hours
		else returnable += `${minutes}:` // means that we don't already have hours
	}

	if (secsMatch) {
		seconds = secsMatch[1];
		if (oneDigit.includes(Number(seconds))) seconds = `0${seconds}`;
	}
	else {
		// the seconds value should always be present there
		seconds = `00`;
	}
	returnable += `${seconds}`;

	return returnable
}

export function formatViews(views: number): string {
	/*
		* formats the views in the form of 1.5k or 2.5M
		* we first divide the views by 1000, for ex. 253678 becomes 253.678. We then multiply it by 10 to round it off to the 1st decimal -> it becomes 2536.78. Then we take Math.round on it so that it's rounded off to the nearest integer. Our number becomes 2537. We then divide it by 10 to get the final view count rounded to the first decimal such that it becomes 253.7. We can now stop and attach a 'k' at the end. But we can also do Math.ceil() and get 254k instead of 253.7k views. I think that's cleaner but I will not do that with the million viewcount and above, since 1.6M views is more accurate than 2M views. It just depends on where accuracy is required. This problem hits on lower view counts too - because we're using Math.ceil, a view count like 2653 will get "swollen" to 3k views.
	*/

	let returnableViews: string = '';
	if (views >= 1000 && views < 1000000) {
		returnableViews = `${Math.ceil(Math.round((views/1000) * 10) / 10)}k`;
	}
	else if (views >= 1000000) {
		returnableViews = `${(Math.round((views/1000000) * 10) / 10)}M`;
	}
	return returnableViews;
}
