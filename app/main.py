# Change these lines:
from stimuli_player import load_and_play_sound
from tap_recorder import TapRecorder
from ui import show_instructions
import pygame
import os
from analysis import analyze_taps, print_analysis

def choose_stimulus():
    """List available stimuli and let user choose one."""
    stimuli_folder = "stimuli"
    stimuli_files = [f for f in os.listdir(stimuli_folder) if f.endswith(".wav")]
    
    print("\nAvailable Stimuli:")
    for idx, file in enumerate(stimuli_files, start=1):
        print(f"{idx}. {file}")
    
    choice = int(input("\nEnter the number of the stimulus you want to tap along with: ")) - 1
    return os.path.join(stimuli_folder, stimuli_files[choice])

def get_next_participant_filename():
    """Auto-generate a new participant file name."""
    data_folder = "data"
    existing_files = [f for f in os.listdir(data_folder) if f.startswith("anonymized_participant")]
    next_num = len(existing_files) + 1
    return os.path.join(data_folder, f"anonymized_participant_{next_num:03}.csv")



def main():
    # Initialize Pygame
    pygame.init()

    # Set up display
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Sensorimotor Synchronization Tapping App")

    # Show instructions
    show_instructions(screen)

    # Choose stimulus
    stimulus_path = choose_stimulus()

    # Get output file path
    output_path = get_next_participant_filename()

    # Prepare tap recorder
    tap_recorder = TapRecorder()
    tap_recorder.start()

    # Play sound
    sound = load_and_play_sound(stimulus_path)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tap_recorder.record_tap()

        # Stop when sound is done
        if not pygame.mixer.get_busy():
            running = False

    # Save taps
    tap_recorder.save_to_csv(output_path)
    analysis_result = analyze_taps(tap_recorder.taps)
    print_analysis(analysis_result)
    # Quit
    pygame.quit()

if __name__ == "__main__":
    main()







# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((600, 400))
#     pygame.display.set_caption("Sensorimotor Synchronization Tapping App")

#     show_instructions(screen)

#     stimulus_path = choose_stimulus()
#     output_path = get_next_participant_filename()

#     tap_recorder = TapRecorder()
#     tap_recorder.start()

#     sound = load_and_play_sound(stimulus_path)

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     tap_recorder.record_tap()

#         if not pygame.mixer.get_busy():
#             running = False

#     # Save taps after sound ends
#     tap_recorder.save_to_csv(output_path)

#     # 🔥 ADD THIS PART AFTER SAVING
#     analysis_result = analyze_taps(tap_recorder.taps)
#     print_analysis(analysis_result)

#     pygame.quit()

# if __name__ == "__main__":
#     main()
