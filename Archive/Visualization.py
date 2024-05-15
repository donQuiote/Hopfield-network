import matplotlib.pyplot as plt
import matplotlib.animation as anim


def save_video(state_list, out_path):
    """
    @summary: save_video creates an animation of a the list received.
            This list contains multiple arrays, each one of them is a converted into a frame.
            Afterwards, it stores the video into the file it's being used under the name out_path received.
    @param state_list: A list of pattern image to be converted in the animation.
    @param out_path: The name of the file (format mp4) where the animation is saved.
    @note: Create a animation video of the network state converging to a memorized pattern.
    """
    writer = anim.FFMpegWriter(fps=3,metadata=dict(artist='Me'),bitrate=2000)
    frames = []
    fig = plt.figure()
    for i in range(len(state_list)):
        frames.append([plt.imshow(state_list[i], cmap = 'gray')])

    animation = anim.ArtistAnimation(fig,frames)
    animation.save(out_path)
