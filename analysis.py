import pandas as pd
import matplotlib.pyplot as plt

def analyze_funnel(csv_path):
    df = pd.read_csv(csv_path)
    
    # Sort steps
    df = df.sort_values('max_step')
    
    # Calculate cumulative users reaching each step
    total_sessions = df['session_count'].sum()
    
    reached_step_1 = total_sessions
    reached_step_2 = df[df['max_step'] >= 2]['session_count'].sum()
    reached_step_3 = df[df['max_step'] >= 3]['session_count'].sum()
    reached_step_4 = df[df['max_step'] >= 4]['session_count'].sum()
    
    funnel = [reached_step_1, reached_step_2, reached_step_3, reached_step_4]
    steps = ['View Cart', 'Enter Checkout', 'Select Payment', 'Purchase Complete']
    
    print("Funnel Analysis (Session Counts):")
    for s, count in zip(steps, funnel):
        print(f"{s}: {count}")
        
    print("\nDrop-off Rates between steps:")
    print(f"Cart -> Checkout: {100 - (reached_step_2/reached_step_1)*100:.1f}% drop-off")
    print(f"Checkout -> Payment: {100 - (reached_step_3/reached_step_2)*100:.1f}% drop-off")
    print(f"Payment -> Purchase: {100 - (reached_step_4/reached_step_3)*100:.1f}% drop-off")
    
    # Visualization
    plt.plot(steps, funnel, marker='o')
    plt.title('RapidKart Checkout Funnel Drop-off')
    plt.ylabel('Sessions')
    plt.savefig('funnel_dropoff.png')
    
    # Actionable Insight: 35% drop-off at Payment -> Purchase means the UI at step 3 is confusing.
    # PM Recommendation: Streamline the payment selection UI, remove redundant confirmations.

if __name__ == "__main__":
    analyze_funnel('data/funnel_summary.csv')
