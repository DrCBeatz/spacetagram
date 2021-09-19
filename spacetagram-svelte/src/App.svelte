<script>
	import {store} from './stores/store'

	import Card from './components/ui/Card.svelte';
	import Error from './components/ui/Error.svelte';
	import Button from './components/ui/Button.svelte';
	import Header from './components/ui/Header.svelte';
	import LoadingSpinner from './components/ui/LoadingSpinner.svelte';
	
	import ImageLoader from './components/image/ImageLoader.svelte';
	
	import { fade, fly } from 'svelte/transition';
	
	const RANDOM_IMAGES = "Random Images";
	const IMAGE_DATE_RANGE = "Image Date Range";
	const DATE_TODAY = new Date().toISOString().split("T")[0];
	const DATE_YESTERDAY = new Date(new Date().setDate(new Date().getDate()-1)).toISOString().split("T")[0];
	const API_KEY = 'your_key_here';
	const MAX_IMAGES = 10;

	let mode = RANDOM_IMAGES;
	let imageList = [];
	let likedImages = $store;
	let isLoading = false;
	let error;
	let imageStartDate = DATE_YESTERDAY;
	let imageEndDate = DATE_TODAY;
	let count = 2;


	function loadImages() {
		
		if (!isValidSearch() ) {
			return;
		}

		isLoading = true;
		let request = '';
		if ( mode == RANDOM_IMAGES ) {
			request = `https://api.nasa.gov/planetary/apod?api_key=${API_KEY}&count=${count}`;
		} else {
			request = `https://api.nasa.gov/planetary/apod?api_key=${API_KEY}&start_date=${imageStartDate}&end_date=${imageEndDate}`;
		}

		fetch(request)
	  .then(res => {
		if (!res.ok) {
			isLoading = false;
		  throw new Error("Fetching images failed, please try again later!");
		}
			return res.json();
	  })
	  .then(
		  data => {
			imageList = data.reverse();
			setTimeout(() => {
		  isLoading = false;
		}, 500);
		}	
	  )
	  .catch(err => {
		error = err;
		error.message = "Fetching images failed, please try again later!";
		isLoading = false;
		console.log(err);
	  });
	}

	function isValidSearch () {
    if (mode == RANDOM_IMAGES && count > MAX_IMAGES) {
      error = {message: "Cannot load more than " + MAX_IMAGES + " random images!"};
      return false;
    } else if (mode == RANDOM_IMAGES && count < 1 ) {
        error = {message: "Must load at least 1 random image, i.e. a number greater than 0!"};
          return false;
    } else if (mode == RANDOM_IMAGES && !Number.isInteger(count)) {
        error = {message: "Please enter an integer (no decimals)!"};
          return false;
    }
    if ( mode == IMAGE_DATE_RANGE && imageEndDate > DATE_TODAY) {
        error = {message: "End date must not be greater than today!"};
          return false;
    } 
    else if ( mode == IMAGE_DATE_RANGE && imageStartDate > DATE_TODAY ) {
        error = {message: "Start date must not be greater than today!"};
          return false;
    }
    else if ( mode == IMAGE_DATE_RANGE && imageStartDate > imageEndDate) {
        error = {message: "Start date must not be greater than end date!"}
        return false;
    } 
    if ( mode == IMAGE_DATE_RANGE && daysBetween(imageStartDate, imageEndDate) > MAX_IMAGES) {
        error = {message: "Cannot load more than " + MAX_IMAGES + " days of images!"}
        return false;
    }
    return true;
}	

	function likeImage(image) {
		likedImages = [...likedImages, image]
		store.update((prev) => [...prev, image])
	}

	function removeLikedImage(image) {
		likedImages = likedImages.filter( obj => {
    		return obj.date !== image.date;
		});
		store.update((prev) => [...likedImages])
	}

	function toggleLikedImageHandler(image) {
		if (likedImages.filter(e => e.date === image.date).length > 0 ) {
			removeLikedImage(image);
			return;
		} 
		else {
				likeImage(image);			
		}
	}

	function SendLinkByMail(image) {
				const linebreak = '\r\n\r\n'
                let body = `Check out this ${image.media_type} from NASA's Astronomy Picture of the Day API:` + linebreak;
				if (image.media_type == 'image') {
					body += image.hdurl + linebreak;
				} else {
					body += image.url + linebreak;
				}
				body += image.title + ' - (published ' + image.date + ')' + linebreak;
				body += '"' + image.explanation + '"';
                let uri = "mailto:?subject=";
                uri += encodeURIComponent(image.title + ` (${image.media_type} from NASA)`);
                uri += "&body=";
                uri += encodeURIComponent(body);
				window.location.href = uri 
            }

			function toggleModeHandler () {
				if (mode == RANDOM_IMAGES) {
					mode = IMAGE_DATE_RANGE
				} else {
					mode = RANDOM_IMAGES
				}
			}

			function addDays(date, days) {
    			return new Date(
        			date.getFullYear(),
					date.getMonth(),
					date.getDate() + days,
					date.getHours(),
					date.getMinutes(),
					date.getSeconds(),
					date.getMilliseconds()
    			);
			}

			function clearError() {
	 			 error = null;
			}

			function treatAsUTC(date) {
    			var result = new Date(date);
    			result.setMinutes(result.getMinutes() - result.getTimezoneOffset());
    			return result;
			}

			function daysBetween(startDate, endDate) {
    			var millisecondsPerDay = 24 * 60 * 60 * 1000;
    			return (treatAsUTC(endDate) - treatAsUTC(startDate)) / millisecondsPerDay;
			}


			loadImages();
</script>

<style>
* {
  box-sizing: border-box;
}


/* .column {
	float: left;
	width: 50%;
	padding: 0 10px;
}

.row:after {
	content: "";
	display: table;
	clear: both;
}

.row {margin: 0 -5px;}

@media screen and (max-width: 600px) {
	.column {
		width: 100%;
		display: block;
		margin-bottom: 20px;
	}
}

.responsive {
	max-width: 100%;
	height: auto;
} */

input[type='number']{
	width: 80px;
} 

.center-button {
	margin:0 auto;
    display:block;
}

h1 { 
	font-family: "Roboto Slab", serif;
	color:white;	
}

h3 { 
	color: #808080;
}

.heart-container {
  height: 20px;
}

.heart-icon {
	margin-top: -10px;
	height: 30px;
}

.container {
	position: relative;
	overflow: hidden;
  width: 100%;
  padding-top: 56.25%; 
}

.responsive-iframe {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  height: 100%;
}

main {
    font-family: sans-serif;
    text-align: center;
    overflow: hidden;
    height: 10rem;
		display: grid;
  }

.el1,
  .el2 {
    height: 5em;
		grid-column: 1/2;
		grid-row: 1/2
  }

</style>

{#if error}
	<Error message={error.message} on:cancel={clearError} />
{/if}

<Header>
	<div slot="search">
		<Button mode="outline success" on:click={loadImages}>Load Images</Button>

</div>
	<div slot="title">Spacetagram</div>
</Header>

{#if isLoading } 
	<LoadingSpinner />
	<!-- <h1 class="center-text">Loading... Please wait!</h1> -->
{:else}

<section transition:fade>
			{#if imageList.length > 0 }
		<h1 class="center-text">NASA's Astronomy Picture of the Day</h1>
	{:else}
	<h1 class="center-text">No images found, try again with a different start and end date.</h1>	
	{/if}
		<h5 class="center-text" style="color:white">(choose search options below and click 'Load Images' above for more images)</h5>
		<h3 class="center-text" style="color:white">Toggle Search Mode:</h3>
		<Button mode="center-button" on:click={toggleModeHandler}>{mode}</Button>
		<br>
		</section>
		<main>
		{#if mode == IMAGE_DATE_RANGE}

		<div class="el1" in:fly={{ x: 100, duration: 400, delay: 150 }} 
		out:fly={{ x: 100, duration: 400 }}>
			<label style="color:white" for="start-date">Start date:</label>
			<input type="date" id="start-date" name="start-date" bind:value={imageStartDate} max={DATE_TODAY} />

			<label style="color:white" for="end-date">End date:</label>
			<input type="date" id="end-date" name="end-date" bind:value={imageEndDate} max={DATE_TODAY} />
		</div>
		{:else}
		<div class="el2" in:fly={{ x: 100, duration: 400, delay: 150 }} 
		out:fly={{ x: 100, duration: 400 }}>
		
		<p style="color:white"># of images:</p>
		<input name="count" type="number" min="1" max="10" bind:value={count} />
		</div>
		{/if}
	</main>
		
		
	{#each imageList as image}
	<Card>
		<div transition:fade>
		<h3 class="center-text">{image.title} - ({image.date})</h3> 
		{#if image.media_type == 'image'}
		<a href={image.hdurl} target="_blank" >
		<ImageLoader src={image.url} alt={image.title} />
		</a>
		{:else if image.media_type = 'video'}
		<div class="container">
		<iframe title={image.title} class="responsive-iframe" width="420" height="315" allow="fullscreen;" allowfullscreen src={image.url}></iframe>
		</div>
		{:else}
		<a href={image.url}>{image.url}</a>
		{/if}
		<br>
		<div transition:fade>
		{#if image.media_type == 'image'}
		<Button mode="outline success" on:click={SendLinkByMail(image)}>Email Image URL</Button>
		{:else if image.media_type == 'video'}
		<Button mode="outline success" on:click={SendLinkByMail(image)}>Email Video URL</Button>
		{:else}
		<Button mode="outline success" on:click={SendLinkByMail(image)}>Email URL</Button>
		{/if}
		<p>{image.explanation}</p>
		<p>
			<!-- <Button mode={(likedImages.filter(e => e.date === image.date).length > 0 ) ? "button outline" : "outline success"} on:click={toggleLikedImageHandler(image)}  -->
				<!-- id={image.date} -->
			<Button mode="outline success" on:click={toggleLikedImageHandler(image)} 	
				 
				>{(likedImages.filter(e => e.date === image.date).length > 0 ) ? 'Unlike' : ' Like '}</Button>
				
				<br>
				<div class="heart-container">
				{#if (likedImages.filter(e => e.date === image.date).length > 0 )}
					<img class="heart-icon" transition:fade src="https://www.spacetagram.io/static/img/heart3.png" alt="Heart Icon" />
					{/if}
				</div>
			</div>
	</div>
	</Card>
	{/each}
{/if}