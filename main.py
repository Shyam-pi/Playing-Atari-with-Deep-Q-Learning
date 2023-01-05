import argparse
from test import test
from environment import Environment
import warnings
warnings.filterwarnings("ignore")


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder_name',default=None)
    parser.add_argument('--model_path',default=None)
    parser.add_argument('--env_name', default=None, help='environment name')

    parser.add_argument('--train_dqn', action='store_true', help='whether train DQN')
    parser.add_argument('--continue_train', action='store_true', help='whether continue to train')
    parser.add_argument('--test_dqn', action='store_true', help='whether test DQN')

    parser.add_argument('--video_dir', default=None, help="output video directory")
    parser.add_argument('--do_render', action='store_true', help='whether render environment')

    args = parser.parse_args()
    return args


def run(args):

    "******Deep Q Learning******"
    if args.train_dqn:
        env_name = args.env_name or 'AssaultNoFrameskip-v0'
        env = Environment(env_name, args, atari_wrapper=True)
        from agent_dir.agent_dqn import AgentDQN
        agent = AgentDQN(env, args)
        agent.train()

    if args.test_dqn:
        env_name = args.env_name or 'AssaultNoFrameskip-v0'
        env = Environment(env_name, args, atari_wrapper=True, test=True)
        from agent_dir.agent_dqn import AgentDQN
        agent = AgentDQN(env, args)
        test(agent, env, total_episodes=100)

if __name__ == '__main__':
    args = parse()
    run(args)
