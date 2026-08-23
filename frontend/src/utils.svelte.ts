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

export function count(data: APIdata): [Array<string>, number, Array<Video[]>] {
	const genres = Object.keys(data);
	const videos = Object.values(data);
	let videoCount: number = 0;

	for (let i = 0; i < videos.length; i++) {
		const genreVideos: Array<Video> = videos[i];
		for (let j = 0; j < genreVideos.length; j++) {
			videoCount += 1
		}
	}
	return [genres, videoCount, videos];
}

export function giveGenreDescription(genre: string): string {
	/*
		* Just returns a genre description for every genre in the genre list
	*/
	if (genre === "Mixed Bag") return "A little bit of everything, like normal YouTube";
	else if (genre === "Countries and Progress") return "Stories about countries, their systems and idiosyncrasies";
	else if (genre === "Money and World Models") return "Videos related to economics, and models for the real world";
	else if (genre === "Dark History") return "Where history meets horror..";
	else if (genre === "Video Essays") return "Essays about essentially any topic you can think of";
	else if (genre === "Earth and Anomlaies") return "Stories about our planet, its geography, and some mysteries related to the same";
	else if (genre === "Health and Lifestyle") return "Small habits, better you"; // to be renamed to health and lifestyle
	else if (genre === "Horror Games") return "Video games, but the ones that spook you out";
	else if (genre === "General Gaming") return "Press start on something better";
	else if (genre === "Philosophy") return '"The unexmained life is not worth living" - Socrates';
	else if (genre === "Mindset and Thinking") return "Rewire the way you think";
	else if (genre === "Food") return "What's cooking?";
	else if (genre === "Linux and Tooling") return "fuck you NVIDIA";
	else if (genre === "Programming") return "Talk is cheap. Show me the code."; 
	else if (genre === "Animation and Culture") return "Animated selections and videos about culture";
	else if (genre === "Learning and Productivity") return "What would you like to learn today?"; // maybe renamed
	else if (genre === "Creativity") return "What the AIs cannot do"; // maybe renamed
	else if (genre === "Physics") return "Reality, decoded";
	else if (genre === "Mathematics") return "The language of the universe";
	else if (genre === "Technology") return "Speedrunning p(doom)..";
	else if (genre === "Pokémon") return "Gotta catch 'em all!";
	else if (genre === "The Sounds of Life") return "Curation on music and life";
	// else if (genre === "The Internet") return "...minus the brainrot (hopefully)";
	else return "..minus the brainrot (hopefully)";
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
		// if (returnable.indexOf(':') !== -1) returnable += `${minutes}:` // means that we already have hours
	}
	else {
		minutes = `00`;
	}
	returnable += `${minutes}:`;

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
		* we first divide the views by 1000, for ex. 253678 becomes 253.678. We then multiply it by 10 to round it off to the 1st decimal -> it becomes 2536.78. Then we take Math.round on it so that it's rounded off to the nearest integer. Our number becomes 2537. 
		* We then divide it by 10 to get the final view count rounded to the first decimal such that it becomes 253.7. We can now stop and attach a 'k' at the end. But we can also do Math.ceil() and get 254k instead of 253.7k views. 
		* I think that's cleaner but I will not do that with the million viewcount and above, since 1.6M views is more accurate than 2M views. It just depends on where accuracy is required. 
		* This problem hits on lower view counts too - because we're using Math.ceil, a view count like 2653 will get "swollen" to 3k views. Might I want to apply this to only 100k+ views?
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

function getRandomInteger(max: number): number {
	return Math.floor(Math.random() * max);
}

export function shuffle(array: Array<any>): Array<any> {
	/*
		* Randomises an array
		* Use case is genre randomisation, or video randomisation
		* Causes an infinite loop when we feed in duplicate items
		* See Knuth shuffle
	*/
	const newArray: Array<any>  = [];
	while (newArray.length !== array.length) {
		const randomItem = array[getRandomInteger(array.length)];
		if (!(newArray.includes(randomItem))) newArray.push(randomItem); // push the randomItem to the new array only when it is not already in it
		// do this until the new array's length is not equal to the original array's length
	}
	return newArray;
}
