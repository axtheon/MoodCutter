from audio.laughter_detector import detect_loud_moments
import matplotlib.pyplot as plt

AUDIO_FILE = "./examples/audio/test_audio.wav"
CHUNK_DURATION = 0.5  # Analyze audio in 0.5 second chunks
THRESHOLD_MULTIPLIER = 1.5  # Loud moments are 1.5x average energy

def main():
    # Detect loud moments in the audio file
    result = detect_loud_moments(
        AUDIO_FILE,
        CHUNK_DURATION,
        THRESHOLD_MULTIPLIER
    )

    print("Audio Loaded")
    print(f"Sample Rate: {result['sample_rate']} Hz")
    print(f"Duration: {result['duration']:.2f} seconds\n")

    # Display detected loud moments
    print("Loud Moments Detected:")
    if not result["loud_moments"]:
        print("None")
    else:
        for start, end in result["loud_moments"]:
            print(f"{start:.2f}s → {end:.2f}s")

    # Visualize energy levels over time
    plt.figure(figsize=(12, 4))
    plt.bar(result["times"], result["energies"], width=CHUNK_DURATION)
    plt.axhline(color="red", y=result["threshold"], linestyle="--", label="Threshold")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Energy (Loudness)")
    plt.title("Laughter Detection v0.1")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
