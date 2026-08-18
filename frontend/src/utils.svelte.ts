type APIdata = {
	[genre: string]: Video[];
}

type Video = {
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

export function count(data: APIdata): [string[], number] {
	const genres = Object.keys(data);
	const videos = Object.values(data);
	let videoCount: number = 0;
	console.log(genres);

	for (let i = 0; i < videos.length; i++) {
		const genreVideos: Video[] = videos[i];
		for (let j = 0; j < genreVideos.length; j++) {
			videoCount += 1
		}
	}
	return [genres, videoCount];
}
