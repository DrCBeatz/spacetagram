<script>
	import Card from './Card.svelte';
	import Badge from './Badge.svelte';
	import Button from './Button.svelte';
	import Header from './Header.svelte';
	import LoadingSpinner from './LoadingSpinner.svelte';

	import {store} from './stores/store'

	import { fade, fly } from 'svelte/transition';

	const RANDOM_IMAGES = "Random Images";
	const IMAGE_DATE_RANGE = "Image Date Range";
	const DATE_TODAY = new Date().toISOString().split("T")[0];
	const DATE_YESTERDAY = new Date(new Date().setDate(new Date().getDate()-1)).toISOString().split("T")[0];
	// const DAY_BEFORE_TODAY = addDays(DATE_TODAY, 1);

	let mode = RANDOM_IMAGES;
	let search = '';
	let imageList = [];
	let likedImages = $store;
	// let likedImages = store.get();
	let isLoading = false;
	let imageStartDate = DATE_YESTERDAY; // addDays(DATE_TODAY, -1);
	let imageEndDate = DATE_TODAY;
	let count = 2;

	

	function loadImages() {
		let request = '';
		if ( mode == RANDOM_IMAGES ) {
			request = `https://api.nasa.gov/planetary/apod?api_key=dAt0hYR1btozyhNwVCih2alU4bwYFljIrmWtQ4JW&count=${count}`;
		} else {
			request = `https://api.nasa.gov/planetary/apod?api_key=dAt0hYR1btozyhNwVCih2alU4bwYFljIrmWtQ4JW&start_date=${imageStartDate}&end_date=${imageEndDate}`;
		}

		fetch(request)
	  .then(res => {
		  isLoading = true;
		if (!res.ok) {
		  throw new Error("Fetching images failed, please try again later!");
		}
		return res.json();
	  })
	  .then(
		  data => {
			imageList = data.reverse();
			setTimeout(() => {
		  isLoading = false;
		//   meetups.setMeetups(loadedMeetups.reverse());
		}, 500);
								}	
	  )
	  .catch(err => {
		error = err;
		console.log(err);
	  });
	}

	function likeImage(image) {
		console.log(image);
		likedImages = [...likedImages, image]
		store.update((prev) => [...prev, image])
		console.log(store);
	}

	function removeLikedImage(image) {
		likedImages = likedImages.filter( obj => {
			// document.getElementById(image.date).disabled = false;
    		return obj.date !== image.date;
		});
		console.log(likedImages);
		// store[0].update((images) => images.filter((item) => item.date !== image.date))
		store.update((prev) => [...likedImages])
		console.log(store);
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

	// $: if (likedImages.length >= 5) {
	// 	maxNominees = true;
	// } else {
	// 	maxNominees = false;
	// }

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
                // window.open(uri);
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

			// const datePicker = getElementById('#datePickerId');

			// datePicker.max = new Date().toISOString().split("T")[0];
			loadImages();
</script>

<style>
* {
  box-sizing: border-box;
}
	  #my-nominees {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr;
    grid-gap: 1rem;
  }

  .column {
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
img { 
display: block;
  margin-left: auto;
  margin-right: auto;
  /* width: 50%; */
}

.responsive {
  max-width: 100%;
  height: auto;
}

input[type='number']{
    width: 80px;
} 

.center-text {
  text-align: center;
}

.center-button {
    margin:0 auto;
    display:block;
}

.heart-center {
	margin: auto;
    padding: 20px;
}

.form {
  display: flex;
  flex-direction: row;
}
.search-field {
	background-color: #f6f6f6;
  width: 100%;
  padding: 10px 35px 10px 15px;
  border: 3px black;
  border-radius: 100px;
  outline: 3px ;
}

.search-button {
  background: transparent;
  border: none;
  outline: none;
  margin-left: -33px;
}

.search-button img {
  width: 20px;
  height: 20px;
  object-fit: cover;
}

h1 { 
	font-family: "Roboto Slab", serif;
	color:white;
}


h3 { 
	color: #808080;
}

.heart {
  width:200px;
  background:
   radial-gradient(circle at 60% 65%, #cf0056 64%, transparent 65%) top left,
   radial-gradient(circle at 40% 65%, #cf0056 64%, transparent 65%) top right,
   linear-gradient(to bottom left, #cf0056 43%,transparent 43%) bottom left ,
   linear-gradient(to bottom right,#cf0056 43%,transparent 43%) bottom right;
  background-size:50% 50%;
  background-repeat:no-repeat;
  display:inline-block;
}
.heart::before {
  content:"";
  display:block;
  padding-top:100%;
}

.label {
	color: black;
}

.container {
  position: relative;
  overflow: hidden;
  width: 100%;
  padding-top: 56.25%; /* 16:9 Aspect Ratio (divide 9 by 16 = 0.5625) */
}

/* Then style the iframe to fit in the container div with full height and width */
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

<Header>
	<div slot="search">
		<Button mode="outline" on:click={loadImages}>Load Images</Button>

</div>
	<div slot="title">Spacetagram</div>
</Header>

{#if isLoading } 
	<LoadingSpinner />
{:else}

	{#if imageList.length > 0 }
		<section transition:fade>
		<h1 class="center-text">NASA's Astronomy Picture of the Day</h1>
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
		<img src={image.url} alt={image.title} class="responsive" max-height="500" max-width="1000"/>
		</a>
		{:else if image.media_type = 'video'}
		<div class="container">
		<iframe class="responsive-iframe" width="420" height="315" src={image.url}></iframe>
		</div>
		{:else}
		<a href={image.url}>{image.url}</a>
		{/if}
		<br>
		{#if image.media_type == 'image'}
		<Button mode="center-button outline success" on:click={SendLinkByMail(image)}>Email Image URL</Button>
		{:else if image.media_type == 'video'}
		<Button mode="center-button outline success" on:click={SendLinkByMail(image)}>Email Video URL</Button>
		{:else}
		<Button mode="center-button outline success" on:click={SendLinkByMail(image)}>Email URL</Button>
		{/if}
		<p>{image.explanation}</p>
		<p>
			<Button mode={(likedImages.filter(e => e.date === image.date).length > 0 ) ? "button outline" : "outline success"} on:click={toggleLikedImageHandler(image)} 
				
				id={image.date} 
				>{(likedImages.filter(e => e.date === image.date).length > 0 ) ? 'Unlike' : ' Like '}</Button>
				
				<br>
				{#if (likedImages.filter(e => e.date === image.date).length > 0 )}
				<div in:fade out:fade class="heart" style="width:30px;display:inline-block"></div>
			{/if}

	</div>
	</Card>
	{/each}
	<!-- {:else} -->
	<!-- <h1 class="center-text">Welcome to Spacetagram!</h1> -->
	<!-- <h3 class="center-text">Images from NASA's Astronomy Picture of the Day</h3> -->
		<!-- <h5 class="center-text">Enter the number of images to load (above) and click "Load Images".</h5> -->
	{/if}
	


{/if}