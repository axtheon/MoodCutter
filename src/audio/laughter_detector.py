import librosa
import numpy as np

def detect_loud_moments(audio_path, chunk_duration, threshold_multiplier):
    # Load audio file and get sample rate
    audio, sr = librosa.load(audio_path)

    # Calculate total duration and chunk parameters
    duration = len(audio) / sr
    chunk_size = int(sr * chunk_duration)
    num_chunks = len(audio) // chunk_size

    energies = []
    times = []

    # Process audio in chunks
    for i in range(num_chunks):
        start = i * chunk_size
        end = start + chunk_size
        chunk = audio[start:end]

        # Calculate RMS energy (loudness) for this chunk
        energy = np.sqrt(np.mean(chunk ** 2))
        energies.append(energy)
        times.append(i * chunk_duration)

    # Calculate dynamic threshold based on average energy
    avg_energy = np.mean(energies)
    threshold = threshold_multiplier * avg_energy

    # Identify chunks that exceed the threshold
    loud_moments = []
    for i, e in enumerate(energies):
        if e > threshold:
            loud_moments.append((times[i], times[i] + chunk_duration))

    return {
        "sample_rate": sr,
        "duration": duration,
        "energies": energies,
        "times": times,
        "threshold": threshold,
        "loud_moments": loud_moments
    }
